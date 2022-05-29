import asyncio
import sys
import pyTextColor as color
import os.path as path

from lib import Plot


async def call():
    searchObject = Plot(sys.argv[1])
    result = await searchObject.get_plot()
    txt = color.pyTextColor()

    if result is None:
        print(txt.format_text(text="Couldn't find movie, Kindly check the name",
                              color="#839496",
                              bgcolor="#DC322F"))
    else:
        titleText = txt.format_text(text=searchObject.name,
                                    color="#6c71c4",
                                    bgcolor="#002b36")

        header = txt.format_text(text="Movie: ",
                                 color="#859900",
                                 bgcolor="#002B36")

        plot_header = txt.format_text(text="Plot: ",
                                      color="#2AA198",
                                      bgcolor="#002B36")
        output = f'{header} {titleText}\n\n\n{plot_header} {result}'
        print(output)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {path.basename(__file__)} <MovieName>")
    else:
        asyncio.run(call())


if __name__ == '__main__':
    main()
