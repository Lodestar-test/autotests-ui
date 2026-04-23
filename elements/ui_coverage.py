from ui_coverage_tool import UICoverageTracker, ActionType, SelectorType

tracker = UICoverageTracker(app="ui-course")

# tracker.track_coverage(
#     selector='#login-button',
#     action_type=ActionType.CLICK,
#     selector_type=SelectorType.XPATH
# )