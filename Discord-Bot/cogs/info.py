import discord
from discord.ext import commands
import psutil


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()

    async def on_ready(self):
        print('Info Cog Loaded Succesfully')

    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        embedvar = discord.Embed(title="Help Commands",
                                 description=None, color=0x00ff00)

        embedvar.add_field(
            name='--info', value='Shows all comands to get info', inline=False)

        embedvar.add_field(
            name='--gen', value='Shows all commands related to gen', inline=False)

        embedvar.add_field(
            name='--extra', value='Shows some extra commands', inline=False)

        embedvar.add_field(
            name='--fun', value='Shows all the fun commands!', inline=False)

        await ctx.send(embed=embedvar)

    @commands.command()
    async def fun(self, ctx):
        embedvar = discord.Embed(title="All the fun commands",
                                 description=None, color=0x00ff00)

        embedvar.add_field(name="--8ball <question>", value="Tell the chances of happening (write the question with it )",
                           inline=False)

        embedvar.add_field(name='--spam <message> <value>',
                           value='Spams the message given', inline=False)

        await ctx.send(embed=embedvar)

    @commands.command()
    async def gen(self, ctx):
        emboo = discord.Embed(title='All the Generator Commands',
                              description=None, color=0x00ff00)

        emboo.add_field(name='--password <length>',
                        value='Generated a password of given length', inline=False)

        await ctx.send(embed=emboo)

    @commands.command()
    async def info(self, ctx):
        emblo = discord.Embed(title='All The Commands to Get Info',
                              description=None, color=0x00ff00)

        emblo.add_field(
            name='--bot', value='Tells the info about bot', inline=False)

        emblo.add_field(name='--server',
                        value='Tells the info about server', inline=False)

        emblo.add_field(name='--user <mention>',
                        value='Tells the info about that user', inline=False)

        emblo.add_field(name='--memcount',
                        value='Shows Total Members in the server', inline=False)

        await ctx.send(embed=emblo)

    @commands.command()
    async def extra(self, ctx):
        emboo = discord.Embed(title='Extra Commands',
                              description=None, color=0x00ff00)

        emboo.add_field(name="--invite",
                        value="Creates a invite", inline=False)

        await ctx.send(embed=emboo)

    @commands.command(aliases=['python', 'botinfo'])
    async def bot(self, ctx):
        values = psutil.virtual_memory()
        val2 = values.available * 0.001
        val3 = val2 * 0.001
        val4 = val3 * 0.001

        values2 = psutil.virtual_memory()
        value21 = values2.total
        values22 = value21 * 0.001
        values23 = values22 * 0.001
        values24 = values23 * 0.001

        # I know i made this shit, you can do this in single line too, i was just converting it to GB.

        embedve = discord.Embed(
            title="Bot Info", description=None, color=0x9370DB)
        embedve.add_field(
            name="Bot Latency", value=f"Bot latency - {round(self.client.latency * 1000)}ms", inline=False)
        embedve.add_field(name='Hosting Stats', value=f'Cpu usage- {psutil.cpu_percent(1)}%'
                          f'\n(Actual Cpu Usage May Differ)'
                          f'\n'

                          f'\nNumber OF Cores - {psutil.cpu_count()} '
                          f'\nNumber of Physical Cores- {psutil.cpu_count(logical=False)}'
                          f'\n'

                          f'\nTotal ram- {round(values24, 2)} GB'
                          f'\nAvailable Ram - {round(val4, 2)} GB')

        await ctx.send(embed=embedve)

    @commands.command(aliases=['user'])
    # Don't go on what i put variable names
    async def _user(self, ctx, member: discord.Member):
        roles = [rrole.name for rrole in member.roles[1:]]

        embedv = discord.Embed(
            title=f"Info About {member.name}", description=None, color=0x00FF00)

        embedv.set_thumbnail(url=member.avatar_url)

        embedv.add_field(
            name="Joined: ", value=f"{member.joined_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}", inline=False)

        embedv.add_field(name="Created: ", value=f"{member.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}",
                         inline=False)

        embedv.add_field(name="Total Roles",
                         value=f"{len(member.roles) - 1}", inline=False)

        embedv.add_field(
            name="Roles", value=f"{' | '.join(roles)}", inline=False)

        embedv.add_field(name='ID', value=f"{member.id}", inline=False)

        await ctx.send(embed=embedv)

    @commands.command()
    async def server(self, ctx):
        roles = [rrole.name for rrole in ctx.guild.roles]

        roles.remove('@everyone') 

        embedva = discord.Embed(title="Info About The Server",
                                description=None, color=0x00FFFF)

        embedva.set_thumbnail(url=ctx.guild.icon_url)

        embedva.add_field(name="Server Name",
                          value=f"{ctx.guild}", inline=False)

        embedva.add_field(
            name="Region", value=f"{ctx.guild.region}", inline=False)

        embedva.add_field(name="Created", value=f"{ctx.guild.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}",
                          inline=False)

        embedva.add_field(
            name="Owner", value=f"{ctx.guild.owner}", inline=False)

        embedva.add_field(
            name="Channels", value=f"There are {len(ctx.guild.channels)} channels", inline=False)

        embedva.add_field(name="Text Channels", value=f"There are {len(ctx.guild.text_channels)} text-channels",
                          inline=False)

        embedva.add_field(name="Voice Channels", value=f"There are {len(ctx.guild.voice_channels)} voice-channels",
                          inline=False)
        embedva.add_field(name="Verification level",
                          value=f"{ctx.guild.verification_level}", inline=False)

        embedva.add_field(
            name="Total Roles", value=f"There are {len(ctx.guild.roles)} roles", inline=False)

        embedva.add_field(
            name="Roles", value=f"{'  |  '.join(roles)}", inline=False)

        embedva.add_field(name="Server ID",
                          value=f"{ctx.guild.id}", inline=False)

        await ctx.send(embed=embedva)

    
    @commands.command()
    async def memcount(self,ctx):
        await ctx.send(f'There are: {ctx.guild.member_count} members in the server')

    
    @commands.command()
    async def invite(self,ctx):
        inv = str(await ctx.channel.create_invite(unique=False))
        await ctx.send(inv)


def setup(client):
    client.add_cog(Info(client))