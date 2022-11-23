# tg-history-finder

Telegram can't search history using chinese...

So, I made python parsing that looks kind of clumsy but at least works.

The way to implement it will always be iterative (as long as I have ideas).

## Usage

You need to export your telegram history to a json file first.

-   In the Telegram Desktop client, open the chat you want to export
-   In the upper right, go to `Options > Export chat history`
-   Unselect all boxes, as photos and other media aren't supported
-   Be sure to have `Format:` set to `JSON`

```bash
python3 telegram_chat_parser.py <file.json>
python3 fuzzy_find.py <file.csv> <message>
```

Will output the message in the Terminal.

But now the displayed format is very bad...
