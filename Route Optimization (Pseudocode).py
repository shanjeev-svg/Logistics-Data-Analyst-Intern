# For each zone, build a distance matrix and solve a simplified VRP
FUNCTION optimize_route(zone_orders, vehicle_capacity):
    distance_matrix = compute_distance_matrix(zone_orders)
    route = nearest_neighbor_construction(distance_matrix)
    route = two_opt_improve(route, distance_matrix)
    IF route.demand > vehicle_capacity:
        route = split_into_subroutes(route, vehicle_capacity)
    RETURN route
 
FOR each zone IN zones:
    best_route[zone] = optimize_route(zone.orders, VEHICLE_CAPACITY)
