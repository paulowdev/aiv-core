import commands
import json

data = json.load(open('../pck-dependencies.json'))
package = data["packages"]["pandas"]

output = commands.getoutput('pip show %s' % package)
# output = commands.getoutput('pip install --no-install %s' % package)
print(output.split("\n")[1].split(":")[1])

try:
    version = output.split("\n")[1].split(":")[1]
    required = output.split("\n")[-1].split(":")[1]
except Exception as e:
    version = ""
    required = ""
    print "error {} in package {}".format(e, package)

if len(required) > 1:
    print package, "-- ****%s***" % required

pkg_dep = required.replace(" ", "").split(",")

# get package dependencies
# print pkg_dep

# running dependencies

for pkg in pkg_dep:
    print pkg
