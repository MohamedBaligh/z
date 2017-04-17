from django.shortcuts import render

from .models import Problem
# Create your views here.
def showproblems(request):
    problems = Problem.objects.all()
    return render(request, 'ProblemSolutionInfra/problems_all.html', {'questions':problems})

def showproblem(request,slug):
    problem = Problem.objects.get(slug=slug)
    return render(request, 'ProblemSolutionInfra/problem.html', {'question':problem})

def showsolutions(request):
    pass

