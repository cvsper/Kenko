from kenkoapp.models import Customer, Carepro

def create_user_by_type(backend, user, response, *args, **kwargs):

	request = backend.strategy.request_data()

	if backend.name == 'facebook':
		avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']
	if request['user_type'] == 'carepro' and not Carepro.objects.filter(user_id=user.id):
		Carepro.objects.create(user_id=user.id, avatar=avatar)

	elif not Customer.objects.filter(user_id=user.id):
		Customer.objects.create(user_id=user.id, avatar=avatar)