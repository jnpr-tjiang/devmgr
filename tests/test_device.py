def test_get_device(client, db, device):
    # test get device
    resp = client.get('/api/v1/devices/%d' % device.id)
    assert resp.status_code == 200

    data = resp.get_json()['device']
    assert data['name'] == device.name
    assert data['serial'] == device.serial
