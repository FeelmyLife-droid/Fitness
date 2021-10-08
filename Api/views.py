import datetime
from typing import Optional

import aiohttp as aiohttp
from asgiref.sync import sync_to_async
from django.http import HttpResponse, HttpRequest, JsonResponse
from pydantic import BaseModel, Field, HttpUrl

from Api.models import Club


class Employes(BaseModel):
    id: Optional[str] = Field(alias="ID")  # "id": "4fc32a32-b06c-11ea-ae96-00155d3c6431",
    name: Optional[str] = Field(alias="FullName")  # "name": "Белухин Степан Евгеньевич",
    position: Optional[str]  # "position": "Инструктор тренажерного зала",
    description: Optional[str] = Field(alias="Description")  # "description": "",
    email: Optional[str] = Field(alias="Email")  # "email": "",
    image_url: Optional[HttpUrl] = Field(
        alias="Photo")  # "imageUrl": "http://89.22.150.56/fitness1c_noauth/hs/nfc_mobile/files/4d9ecf50-0c69-11eb-768c-00155d3c6431.jpeg",
    workingHours: Optional[datetime.time] = Field(alias="workingHours")  # "workingHours": "",
    phone: Optional[str] = Field(alias="Phone")  # "phone": "79166389453",
    coach_id: Optional[str] = Field(alias="ID")
    departments: Optional[list] = []

    def __init__(self, **kwargs):
        kwargs["position"] = kwargs["Position"]["Title"]
        kwargs["departments"] = [{'value': kwargs["Department"][0]['Title'], "position": "Сотрудник"}]
        super().__init__(**kwargs)


async def get_employees(request: HttpRequest, club_id):
    if request.method == 'GET':
        club = await sync_to_async(Club.objects.filter)(pk=club_id)
        club = club.last()
        if not club:
            return HttpResponse(status=404)
        request_data = {
            "Request_id": "e1477272-88d1-4acc-8e03-7008cdedc81e",
            "ClubId": club.club_id,
            "Method": "GetSpecialistList",
            "Parameters": {"ServiceId": ""}

        }

        async with aiohttp.ClientSession() as client:
            async with client.post(url=club.api_url,
                                   auth=aiohttp.BasicAuth(club.username, club.password),
                                   json=request_data) as res:
                resp = await res.json()
                ans = []
                if res.status == 200:
                    for employes in resp['Parameters']:
                        ans.append(Employes(**employes).dict())
        return JsonResponse(data=ans, status=200, safe=False)
