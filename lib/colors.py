class Colors(object):

    colors = {}

    def __init__(self):
        self.colors["normal"] = "\033[0;0;0m"
        self.colors["red"] = "\033[0;37;41m"
        self.colors["green"] = "\033[0;37;42m"
        self.colors["blue"] = "\033[0;37;44m"
        self.colors["purple"] = "\033[0;37;45m"
        self.colors["cyan"] = "\033[0;37;46m"

    def format_text(self, color, text):
        return self.colors[color] + text + self.colors[color]
