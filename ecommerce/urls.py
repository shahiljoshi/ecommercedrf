from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet,ProductViewSet,CartViewSet,OrderViewSet

router = SimpleRouter()

# router.register('users',UserViewSet, basename='user')

router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('cart', CartViewSet, basename='cart')
router.register('order', OrderViewSet, basename='order')


urlpatterns = router.urls