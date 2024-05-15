from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail, ToyList, ToyDetail, AddToyToCat, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
    path('', Home.as_view(), name='home'),  # Route for the home page view
    path('cats/', CatList.as_view(), name='cat-list'),  # Route to list all cats
    path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),  # Route to view details of a specific cat
    path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),  # Route to list and create feedings for a specific cat
    path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),  # Route to view and edit details of a specific feeding
    path('toys/', ToyList.as_view(), name='toy-list'),  # Route to list all toys
    path('toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),  # Route to view details of a specific toy
    path('cats/<int:cat_id>/add_toy/<int:toy_id>/', AddToyToCat.as_view(), name='add-toy-to-cat'), # Route to add a toy to a specific cat
    path('users/register/', CreateUserView.as_view(), name='register'), # Route to register a new user
    path('users/login/', LoginView.as_view(), name='login'), # Route to log in a user
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'), # Route to refresh a user's token
]
