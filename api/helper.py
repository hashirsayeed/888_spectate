from datetime import datetime
import pytz


def get_UTC_time(time, time_zone):
    try:
        time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        temp = pytz.timezone(time_zone)
        temp_t = temp.localize(time)
        utc = temp.normalize(temp_t).astimezone(pytz.utc)
        return utc
    except Exception as e:
        print("Error occured while getting the time zone!", e)
        return None 

def make_filter_sport(filters):
    try:
        sport_filter = " "
        if filters:
            if 'active' in filters:
                sport_filter += " WHERE sport.Active IN " + filters['Active']
            else:
                sport_filter += " WHERE sport.Active = 1"
            if 'id' in filters:
                sport_filter += " AND sport.ID =" + str(filters['id'])
            if 'name' in filters:
                sport_filter += " AND sport.Name LIKE '%" + filters['Name'] + "%'"
            if 'slug' in filters:
                sport_filter += " AND sport.slug LIKE '%" + filters['Slug'] + "%'"
            if 'min_event' in filters:
                sport_filter += " AND (SELECT count(1) FROM event AS event WHERE event.Active = 1 AND event.Sport_id = sport.id) >= " + filters['min_event']
            if 'max_event' in filters:
                sport_filter += " AND (SELECT count(1) FROM event AS event WHERE event.Active = 1 AND event.Sport_id = sport.id) <= " + filters['max_event']
            if 'eq_event' in filters:
                sport_filter += " AND (SELECT count(1) FROM event AS event WHERE event.Active = 1 AND event.Sport_id = sport.id) = " + filters['min_event']
        else:
            sport_filter += " WHERE sport.Active = 1"
        return sport_filter
    except Exception as e:
        print("Exception occured while creating filter for sport: ", e)
        return None

def make_filter_event(filters):
    try:
        event_filter = " "
        if filters:
            if 'active' in filters:
                event_filter += " WHERE event.Active IN " + filters['active']
            else:
                event_filter += " WHERE event.Active = 1"
            if 'id' in filters:
                event_filter += " AND event.ID =" + str(filters['id'])
            if 'name' in filters:
                event_filter += " AND event.Name LIKE '%" + filters['name'] + "%'"
            if 'slug' in filters:
                event_filter += " AND event.Slug LIKE '%" + filters['slug'] + "%'"
            if 'type' in filters:
                event_filter += " AND event.Type LIKE '%" + filters['type'] + "%'"
            if 'status' in filters:
                event_filter += " AND event.Status LIKE '%" + filters['status'] + "%'"
            if 'sport_id' in filters:
                event_filter += " AND event.Sport_id LIKE '%" + filters['sport_id'] + "%'"
            if 'min_event' in filters:
                event_filter += " AND (SELECT count(1) FROM selection AS selection WHERE selection.Active = 1 AND selection.Event_id = event.id) >= " + filters['min_event']
            if 'max_event' in filters:
                event_filter += " AND (SELECT count(1) FROM selection AS selection WHERE selection.Active = 1 AND selection.Event_id = event.id) <= " + filters['max_event']
            if 'eq_event' in filters:
                event_filter += " AND (SELECT count(1) FROM selection AS selection WHERE selection.Active = 1 AND selection.Event_id = event.id) = " + filters['min_event']

            time_zone = ''
            if 'timezone' in filters:
                time_zone = filters['timezone']
            if 'schedule_start' in filters and 'schedule_end' in filters:
                if time_zone:
                   sch_st = get_UTC_time(filters['schedule_start'], time_zone)
                   sch_end = get_UTC_time(filters['schedule_end'], time_zone)
                else:
                    sch_st = filters['schedule_start']
                    sch_end = filters['schedule_end']
                event_filter += " AND event.start_time BETWEEN '" + str(sch_st) + "' AND '" + str(sch_end) + "'"
            elif 'schedule_start' in filters and 'schedule_end' not in filters:
                if time_zone:
                    sch_st = get_UTC_time(filters['schedule_start'], time_zone)
                else:
                    sch_st = filters['schedule_start']
                event_filter += "AND event.start_time >= '" + str(sch_st) + "'"
            elif 'schedule_end' in filters and 'schedule_start' not in filters:
                if time_zone:
                    sch_end = get_UTC_time(filters['schedule_end'], time_zone)
                else:
                    sch_end = filters['schedule_end']
                event_filter += "AND event.start_time <= '" + str(sch_end) + "'"
             
            if 'schedule_ac_start' in filters and 'schedule_ac_end' in filters:
                if time_zone:
                   sch_ac_st = get_UTC_time(filters['schedule_ac_start'], time_zone)
                   sch_ac_end = get_UTC_time(filters['schedule_ac_end'], time_zone)
                else:
                    sch_ac_st = filters['schedule_ac_start']
                    sch_ac_end = filters['schedule_ac_end']
                event_filter += " AND event.actual_start_time BETWEEN '" + str(sch_ac_st) + "' AND '" + str(sch_ac_end) + "'"
            elif 'schedule_ac_start' in filters and 'schedule_ac_end' not in filters:
                if time_zone:
                    sch_ac_st = get_UTC_time(filters['schedule_ac_start'], time_zone)
                else:
                    sch_ac_st = filters['schedule_ac_start']
                event_filter += "AND event.actual_start_time >= '" + str(sch_ac_st) + "'"
            elif 'schedule_ac_end' in filters and 'schedule_ac_start' not in filters:
                if time_zone:
                    sch_ac_end = get_UTC_time(filters['schedule_ac_end'], time_zone)
                else:
                    sch_ac_end = filters['schedule_ac_end']
                event_filter += "AND event.actual_start_time <= '" + str(sch_ac_end) + "'"
        else:
            event_filter += " WHERE event.Active = 1"
        return event_filter
    except Exception as e:
        print("Error occurred while making events filter:", e)
        return None

def make_filter_selection(filters):
    try:
        selection_filter = " "
        if filters:
            if 'active' in filters:
                selection_filter += " WHERE selection.Active IN " + filters['active']
            else:
                selection_filter += " WHERE selection.Active = 1"
            if 'id' in filters:
                selection_filter += " AND selection.ID =" + str(filters['id'])
            if 'name' in filters:
                selection_filter += " AND selection.Name LIKE '%" + filters['name'] + "%'"
            if 'event_id' in filters:
                selection_filter += " AND selection.event_id =" + filters['event_id']
            if 'price' in filters:
                selection_filter += " AND selection.Price =" + filters['price']
            if 'min_price' in filters:
                selection_filter += " AND selection.Price >=" + filters['min_price']
            if 'max_price' in filters:
                selection_filter += " AND selection.Price <=" + filters['min_price']
            if 'outcome' in filters:
                selection_filter += " AND selection.Outcome LIKE '%" + filters['outcome'] + "%'"
        else:
            selection_filter += " WHERE event.Active = 1"
        return selection_filter
    except Exception as e:
        print("Error occurred while making selections filter:", e)
        return None