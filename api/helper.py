def make_filter_sport(filters):
    try:
        sport_filter = " "
        if filters:
            if 'active' in filters:
                sport_filter += " WHERE sport.Active = 1"
            if 'id' in filters:
                sport_filter += " AND sport.ID =" + str(filters['id'])
            if 'name' in filters:
                sport_filter += " AND sport.Name LIKE '%" + filters['name'] + "%'"
            if 'slug' in filters:
                sport_filter += " AND sport.slug LIKE '%" + filters['slug'] + "%'"
            if 'min_event' in filters:
                sport_filter += " AND (SELECT count(1) FROM event as event where event.Active = 1 AND event.Sport_id = sport_id) >= " + filters['min_event']
            if 'max_event' in filters:
                sport_filter += " AND (SELECT count(1) FROM event as event where event.Active = 1 AND event.Sport_id = sport_id) <= " + filters['max_event']
            if 'eq_event' in filters:
                sport_filter += " AND (SELECT count(1) FROM event as event where event.Active = 1 AND event.Sport_id = sport_id) = " + filters['min_event']
        else:
            sport_filter += " WHERE sport.Active = 1"
        return sport_filter
    except Exception as e:
        print("Exception occured while creating filter for sport: ", e)
        return None
