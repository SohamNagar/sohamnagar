# Decorator
def report_format(func):
    def wrapper(self):
        print("=" * 40)
        print("      REPORT GENERATED")
        print("=" * 40)

        func(self)

        print("=" * 40)
        print("       END OF REPORT")
        print("=" * 40)
    return wrapper


# Report Class
class Report:

    # Magic Method
    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    # Class Method
    @classmethod
    def sample_report(cls):
        return cls(
            "Student Report",
            ["Name: Rahul", "Marks: 90", "Grade: A"]
        )

    # Magic Method
    def __str__(self):
        return self.title

    # Decorator Used
    @report_format
    def display(self):
        print("Title:", self.title)
        print("\nSections:")
        for section in self.sections:
            print("-", section)


# Main Program
report = Report.sample_report()
report.display()