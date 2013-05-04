from collective.grok import gs
from kagenomise.policy import MessageFactory as _

@gs.importstep(
    name=u'kagenomise.policy', 
    title=_('kagenomise.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('kagenomise.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
