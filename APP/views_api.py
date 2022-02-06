from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Repo, Hf

def get_repo(request, repoid:int):
    a_repo = Repo.objects.filter(id=repoid).first()
    if a_repo == None:
        return (None, Response(status=status.HTTP_404_NOT_FOUND))
    if not a_repo.tulajdonosa(request.user):
        return (None, Response(status=status.HTTP_403_FORBIDDEN))
    return (a_repo, None)

@api_view(['POST'])
def create_repo(request, hfid):
    a_hf = Hf.objects.filter(id=hfid).first()
    if a_hf == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    a_repo = Repo.objects.create(hf = a_hf, url=request.data['url'])
    return Response({'repoid': a_repo.id})

@api_view(['GET'])
def read_repo(request, repoid:int):
    (a_repo, error) = get_repo(request, repoid)
    if error != None:
        return error
    return Response({'repo_url': a_repo.url})

@api_view(['POST'])
def update_repo(request, repoid):
    (a_repo, error) = get_repo(request, repoid)
    if error != None:
        return error
    a_repo.url = request.data['repo_url']
    a_repo.save()
    return Response(f'a {repoid} id-jű repo url-je módosítva erre: {a_repo.url}')

@api_view(['DELETE'])
def delete_repo(request, repoid):
    (a_repo, error) = get_repo(request, repoid)
    if error != None:
        return error
    a_repo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
