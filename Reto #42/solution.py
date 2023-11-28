def collision(pos_a, vel_a, pos_b, vel_b):
    """
        Collision function to found if two elements collide 
        among them
        :param pos_a: Position of element A
        :param pos_b: Position of element B
        :param vel_a: Speed of element A
        :param vel_b: Speed of element B
        :return str telling if the elements collide or not
    """
    xa, ya = pos_a
    xva, yva = vel_a
    xb, yb = pos_b
    xvb, yvb = vel_b

    if xva == xvb:
        if xa == xb:
            tx = 0
        return "No se van a encontrar"
    else:
        tx = (xb - xa) / (xva - xvb)

    if yva == yvb:
        if ya == yb:
            ty = 0
        return "No se van a encontrar"
    else:
        ty = (yb - ya) / (yva - yvb)
    if tx == ty:
        t = tx
        x = xa + xva * t
        y = ya + yva * t
        return f"Los objetos colisionan en el punto [{x},{y}] en un tiempo {t}"
    return

print(collision((2, 0), (0, 1), (0, 2), (1,0)))
