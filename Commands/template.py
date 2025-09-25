from discord.ext import commands

@commands.command(name="template", help="template guia para apresentação / criação de um projeto, seja lá qual for")
async def template(ctx):
    await ctx.send('''## :bulb: Aqui estão algumas perguntas para apresentação ou desenvolvimento de um projeto:
:man_shrugging: 1 - Que tipo de projeto você está fazendo _(um livro, um jogo, um vídeo, etc)_?

:books: 2 - Do que se trata seu projeto? É ideal que aqui seja feita uma breve descrição do que você planeja fazer.

:family_adult_adult_child_child: 3 - Quantas pessoas serão necessárias para tirar essa ideia do papel?

:abacus: 4 - Quais os requisitos para realização desse projeto? Ele precisa de arte, de música, de programação..?

:hourglass: 5 - Quanto tempo levará, em média, para o projeto ser entregue / concluído?

:money_with_wings: 6 - Caso o seu projeto envolva pessoas além de você, qual valor aproximado será pago aos contribuintes?''')

async def setup(bot):
    bot.add_command(template)