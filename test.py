import pprint
import collections
from rush.models import RushProfile

emails = RushProfile.objects.all().values_list('email', flat=True)
dupes = [item for item, count in collections.Counter(emails).items() if count > 1]
rushes = []
for x in dupes:
	rushes.append(RushProfile.objects.filter(email = x))
pk = [["http://localhost:8000/admin/rush/rushprofile/%d" % x.pk for x in y] for y in rushes]

pprint.pprint(pk)