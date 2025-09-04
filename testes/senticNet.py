from senticnet.babelsenticnet import BabelSenticNet

bsn = BabelSenticNet('pt')
concept_info = bsn.concept('amor')
polarity_label = bsn.polarity_label('você')
polarity_value = bsn.polarity_value('amor')
moodtags = bsn.moodtags('amor')
semantics = bsn.semantics('amor')
sentics = bsn.sentics('amor')


print(polarity_label)
