import subprocess

def html2rst(html):
    p = subprocess.Popen(['pandoc', '--from=html', '--to=rst'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return p.communicate(html)[0]

with open ("um.html", "r") as myfile:
    data=myfile.read().replace('\n', '')

html2rst(data)
