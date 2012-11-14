import settings
for k, _, _ in settings.TESTS:
    print 'scp ~/tmp/%s/flot.js akaariai@vipunen.hut.fi:public_html/djbench/%s/' % (k, k)
    print 'scp ~/tmp/%s/index.html akaariai@vipunen.hut.fi:public_html/djbench/%s/'% (k, k)
