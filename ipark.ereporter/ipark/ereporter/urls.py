from tipfy import Rule

def get_rules():
  return [
      Rule(
        "/internal/ereporter", endpoint="ereporter:send",
        handler="ipark.ereporter.ereporter:SendReport",
      ),
  ]

