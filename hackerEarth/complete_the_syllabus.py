week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
def day_of_complete_syllabus(topic_in_week, topics, topic_count):
    syllabus_complete_day = ''
    if topic_count ==  topics:
        syllabus_complete_day = week_days[0]
    else:
        for topic in range(1, len(topic_in_week)):
            topic_count = topic_in_week[topic] + topic_count
            if topic_count == topics:
                syllabus_complete_day = week_days[topic]
                break
            elif topic_count > topics:
                syllabus_complete_day = week_days[topic - 1]
                break
        if topic_count != topics and topic_count < topics:
            syllabus_complete_day = day_of_complete_syllabus(topic_in_week, topics, topic_count)
    return syllabus_complete_day
test_cases = input()
for test_case in range(test_cases):
    topics = input()
    topic_in_week = [int(i) for i in raw_input().split()]
    topics %= sum(topic_in_week)
    total_days_to_complete_syllabus = day_of_complete_syllabus(topic_in_week, topics, topic_in_week[0])
    print total_days_to_complete_syllabus