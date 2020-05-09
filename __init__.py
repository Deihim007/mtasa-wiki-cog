from .wiki import Wiki

def setup(bot):
    cog = Wiki(bot)
    bot.add_cog(cog)