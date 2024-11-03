import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL) 

embed = Embed(
    color=0xFF4545,
    timestamp='now'
)

image1 = 'https://platform.polygon.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/24528001/bluelock_isagiyoichi.jpeg?quality=90&strip=all&crop=7.8125,0,84.375,100'

embed.set_author(name='Anime Srbija')
embed.add_field(name='Nova epizoda', value='https://www.animesrbija.com/anime/blue-lock-vs-u-20-japan')
embed.set_footer(text='Blue Lock')
embed.set_thumbnail(image1)

hook.send(embed=embed)