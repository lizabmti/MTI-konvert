from pathlib import Path


class ReportWriter:
    @staticmethod
    def save(sessions):
        headings = ["login", "time_in", "time_out"]
        rows = [[s.user, s.time_in, s.time_out or "---"] for s in sessions]
        widths = [max(len(str(row[i])) for row in [headings] + rows) for i in range(3)]
        border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

        def line(cells):
            return "| " + " | ".join(str(v).ljust(w) for v, w in zip(cells, widths)) + " |"

        lines = [border, line(headings), border]
        for row in rows:
            lines.append(line(row))
        lines.append(border)
        Path("otchet.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
