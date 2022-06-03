import discord


def latest(data):
    description = data[0]["articleLead"][0]["html"]
    article = discord.Embed(
        title=f"{data[0]['headline']}",
        url=f"https://www.postimees.ee/{data[0]['id']}/{data[0]['slug']}",
        description=f"{description[3:-4]}",
        color=0x0064FD,
    )

    if "Postimees" in data[0]["authors"][0]["name"]:
        try:
            article.set_author(
                name=f"{data[0]['meta']['exclamation']}",
                url=f"https://www.postimees.ee/author/{data[0]['authors'][0]['id']}",
                icon_url=f"{data[0]['authors'][0]['thumbnail']['sources']['square']['large']}",
            )
        except KeyError:
            pass
    elif len(data[0]["authors"][0]["name"]) < 6:
        article.set_author(
            name=f"{data[0]['authors'][0]['name']}",
            url=f"https://www.postimees.ee/author/{data[0]['authors'][0]['id']}",
            icon_url=f"{data[0]['authors'][0]['thumbnail']['sources']['square']['large']}",
        )
    else:
        try:
            article.set_author(
                name=f"{(data[0]['authors'][0]['name']).replace('Toimetas ', '')} -> {data[0]['authors'][0]['position']}",
                url=f"https://www.postimees.ee/author/{data[0]['authors'][0]['id']}",
                icon_url=f"{data[0]['authors'][0]['thumbnail']['sources']['square']['large']}",
            )
        except (TypeError, KeyError):
            pass

    if data[0]["meta"]["commentCount"] > 1:
        article.add_field(
            name="Comments",
            value=f"{data[0]['meta']['commentCount']}",
            inline=True,
        )

    article.add_field(
        name="Reading Time", value=f"{data[0]['meta']['readingTime']} min"
    )
    article.add_field(
        name="Premium", value=f"{data[0]['isPremium']}", inline=True
    )
    article.add_field(
        name="Category", value=f"{data[0]['sections'][0]['name']}"
    )

    try:
        article.set_image(
            url=f'{data[0]["media"][0]["thumbnail"]["sources"]["landscape"]["large"]}'
        )
    except KeyError:
        article.set_image(
            url=f'{data[0]["media"][0]["sources"]["landscape"]["large"]}'
        )

    article.set_footer(
        text=f"Created at {((data[0]['dateCreated']).replace('T', ' '))[:-9]} | Published at {((data[0]['meta']['actualPublishTime']).replace('T', ' '))[:-9]} | Modified at {((data[0]['dateModified']).replace('T', ' '))[:-9]}"
    )
    return article
