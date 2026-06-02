from fastapi import APIRouter

health_check_router = APIRouter(tags=['health_check'])

@health_check_router.get('/health_check')
def health_check():
    return {'message': 'ok'}
