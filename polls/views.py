from django.db.models import F
from django.http import HttpResponseRedirect  # , Http404, HttpResponse,
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
#
#
# def detail(request, question_id):
#     # return HttpResponse("Você está olhando para a pergunta %s." % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Pergunta não existe")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
#
#
# def results(request, question_id):
#     # response = "Você está olhando os resultados da pergunta %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # return HttpResponse("Você está votando na questão %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    # Este código inclui algumas coisas que ainda não foram cobertas neste tutorial:
    # request.POST é um objeto como dicionários que lhe permite acessar os dados submetidos pelos seus nomes chaves. Neste caso, request.POST['choice'] retorna o ID da opção selecionada, como uma string. Os valores de request.POST são sempre strings.
    # Note que Django também fornece request.GET para acesar dados GET da mesma forma – mas nós estamos usando attr:request.POST <django.http.HttpRequest.POST> explicitamente no nosso código, para garantir que os dados só podem ser alterados por meio de uma chamada POST.
    # request.POST['choice'] irá levantar a exceção KeyError caso uma choice não seja fornecida via dados POST. O código acima checa por KeyError e re-exibe o formulário da enquete com as mensagens de erro se uma choice não for fornecida.
    # F("votes") + 1 instructs the database to increase the vote count by 1.
    # Após incrementar uma opção, o código retorna um class:~django.http.HttpResponseRedirect em vez de um normal HttpResponse. HttpResponseRedirect` recebe um único argumento: a URL para o qual o usuário será redirecionado (veja o ponto seguinte para saber como construímos a URL, neste caso).
    # Como o comentário do Python acima aponta, você deve sempre retornar um depois de lidar com sucesso com Dados POST. Esta dica não é específica para Django; é um bom desenvolvimento web prática em geral.
    # Estamos usando a função reverse() no construtor da HttpResponseRedirect neste exemplo. Essa função nos ajuda a evitar de colocar a URL dentro da view de maneira literal. A ele é dado então o nome da “view” que queremos que ele passe o controle e a parte variável do padrão de formato da URL que aponta para a “view”. Neste caso, usando o URLconf nós definimos em Tutorial 3, esta chamada de reverse() irá retornar uma string como
