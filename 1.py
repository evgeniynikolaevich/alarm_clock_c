
@api_view()
def user_quadrators(request):
    if not request.user.organization:
        raise PermissionDenied()
    if not request.user.cameras_access:
        user_quadrators = []
    else:
        user_quadrators = request.user.cameras_access.get('quadrators', [])
    quadrators_ids = [x['quad'] for x in user_quadrators]
    if not quadrators_ids:
        if request.user.is_staff:
            quadrators_objects = Quadrator.objects.all()
        else:
            quadrators_objects = Quadrator.objects.filter(organization=request.user.organization)
    else:
        quadrators_objects = Quadrator.objects.filter(id__in =quadrators_ids)
    quadrators_group_serializer = QuadratorSerializer(context={'request': request})
    result = {'quadrators':[]}
    for quadrator in quadrators_objects:
        quad_repr = quadrators_group_serializer.to_representation(quadrator)
    return Response(result)

