from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    # pass and confirm을 client에서 받아옴
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    
    # 시리얼라이즈에서 쓰이지 않은 confirm 여기서 확인 작업, 일치 않으면 400 생성
    if password != password_confirmation:
        return Response({ 'error': '비밀번호가 일치하지 않습니다.' }, status=status.HTTP_400_BAD_REQUEST)
    
    # UserSerializer로 데이터 직렬화
    serializer = UserSerializer(data=request.data)

    # vaildation 작업 => password도 같이 직렬화
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 암호화 시키기(해싱)
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)