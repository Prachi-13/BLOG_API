CONNECT API TEMPLATE PACKAGE
============================

* Use generate_api command to generate an api with Create, Read and Update capabilities.

* The generate_api command accepts a parameter `api_name` (name of the api to add).

* Optionally you could also pass `template` parameter, which is defaulted to use `connect_api_template`.


**Note**  
Specify api names to be either singular(E.g `user`) or in snake case(E.g `user_api`).  

E.g usage:
 ```
python manage.py generate_api api_name
 ```

#### Getting the app running
After running above command, a directory structure with the specified `api_name` would be created under project root.
To use this app we need to do a couple more steps.  
Add `api_name` in  `INSTALLED APPS` list under `syrasoft/settings/base`.  
E.g :
```
INSTALLED_APPS = ['api_name.apps.class_name']  
```
**class_name** is  the name of the class ending with Config defined in apps.py under newly created directory.

Next,  
Import and add urls in `syrasoft/settings/urls.py`  
E.g:  
```
from api_name import urls as new_api_name_urls  

urlpatterns = [path('api_name', include(api_name_urls))]
```

Now you are good to go.

**Note**  
You'll have to update the model schema accordingly for each app to function properly.  
There is no Delete end point created, and the user has to implement the same.
