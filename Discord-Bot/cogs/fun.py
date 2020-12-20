from discord.ext import commands
import random
import asyncio


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Cog Loaded Succesfully')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain',
                     'It is decidedly so',
                     'Without a doubt',
                     'Yes, definitely',
                     'You may rely on it',
                     'As i see it, yes',
                     'Most likely',
                     'Outlook good',
                     'Yes',
                     'Signs point to yes',
                     'Reply haze, try again',
                     'Ask again later',
                     'Better not tell you now',
                     'Cannot predict now',
                     'Concentrate and ask again',
                     'Do not count on it',
                     'My reply is no',
                     'My sources say no',
                     'Outlook not so good',
                     'Very doubtful']

        await ctx.send(f'{ctx.author.mention}\n Question: {question} \n Answer: {random.choice(responses)}')

    @commands.command()
    async def spam(self, ctx, message='spam', *, val=5):
        channel_only = self.client.get_channel(758534450191138816)  # Create a channel spam and paste it's id here
        val = int(val)

        if ctx.channel == channel_only and val < 21:

            for i in range(val):
                await ctx.send(f'{message}')
                await asyncio.sleep(0.2)

            await ctx.send(f'{ctx.author.mention} Spamming done')

        elif val > 21 and ctx.channel == channel_only:

            await ctx.send('You Cannot Spam More Than 20 Times')

        else:

            await ctx.send(f'{ctx.author.mention} You cannot use this command here!')
            chan = self.client.get_channel(758534450191138816) # This just sends message to spam channel telling user you can't spam there, spam in this channel
            await chan.send(f'{ctx.author.mention} Spam here')
        

def setup(client):
    client.add_cog(Fun(client))
