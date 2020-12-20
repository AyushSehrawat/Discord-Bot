import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()

    async def on_ready(self):
        print('Mod Cog Loaded Succesfully')

    @commands.command()
    async def pingme(self, ctx):
        await ctx.send(f'{ctx.author.mention}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    # @commands.has_any_role('Owner','Moderators') You can add this if you want some specific roles 
    async def mute(self,ctx,member : discord.Member):
        all_roles = ctx.guild.get_role(757518078270636113)
        await member.remove_roles(all_roles) # Since muted is a second role, it doesn't take effect so we remove rest roles, you have to add all roles here
        muted_role = ctx.guild.get_role(788444564645216266) # Mute role id
        await member.add_roles(muted_role) 
        await ctx.send(f'{member.mention} is muted!')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self,ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addrole(self,ctx, member: discord.Member, rolename: discord.Role):
        if rolename in ctx.guild.roles:
            await member.add_roles(rolename)

        else:
            await ctx.send('Role not found')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unrole(self,ctx, member: discord.Member, rolename: discord.Role):
        if rolename in ctx.guild.roles:

            await member.remove_roles(rolename)

        else:
            await ctx.send('Role not found or User has no such roles')


def setup(client):
    client.add_cog(Mod(client))