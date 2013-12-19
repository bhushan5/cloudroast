from cloudroast.stacktach.fixtures import StackTachFixture


class StackTachTest(StackTachFixture):

    @classmethod
    def setUpClass(cls):
        super(StackTachTest, cls).setUpClass()
        cls.service = 'nova'

    def test_get_event_names(self):
        """
        @summary: Verify that Get Event Names returns 200 Success response
        """
        response = self.stacktach_client.get_event_names()
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.event_name)

    def test_get_host_names(self):
        """
        @summary: Verify that Get Host Names returns 200 Success response
        """
        response = self.stacktach_client.get_host_names()
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.host_name)

    def test_get_deployments(self):
        """
        @summary: Verify that Get Deployments returns 200 Success response
        """
        response = self.stacktach_client.get_deployments()
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.id)
            self.assertIsNotNone(element.name)

    def test_get_timings_summary(self):
        """
        @summary: Verify that Get Timings Summary returns 200 Success response
        """
        response = self.stacktach_client.get_timings_summary()
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.event_name)
            self.assertIsNotNone(element.count)
            self.assertIsNotNone(element.minimum)
            self.assertIsNotNone(element.maximum)
            self.assertIsNotNone(element.average)

    def test_get_kpi(self):
        """
        @summary: Verify that Get KPI returns 200 Success response
        """
        response = self.stacktach_client.get_kpi()
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.event_name)
            self.assertIsNotNone(element.timing)
            self.assertIsNotNone(element.uuid)
            self.assertIsNotNone(element.deployment)

    def test_get_event_id_details(self):
        """
        @summary: Verify that Get Event ID Details returns 200 Success response
        """
        response = (self.stacktach_client
                    .get_event_id_details(event_id=self.event_id,
                                          service=self.service))
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertEqual(len(response.entity), 1,
                         msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.category)
            self.assertIsNotNone(element.publisher)
            self.assertIsNotNone(element.event_id)
            self.assertIsNotNone(element.uuid)
            self.assertIsNotNone(element.service)
            self.assertIsNotNone(element.when)
            self.assertIsNotNone(element.host_name)
            self.assertIsNotNone(element.state)
            self.assertIsNotNone(element.deployment)
            self.assertIsNotNone(element.event_name)
            self.assertIsNotNone(element.actual_event)

    def test_get_timings_for_event_name(self):
        """
        @summary: Verify that Get Timings For Event
            returns 200 Success response
        """
        response = (self.stacktach_client
                    .get_timings_for_event_name("compute.instance.reboot"))
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.event_name)
            self.assertIsNotNone(element.timing)

    def test_get_reports(self):
        """
        @summary: Verify that Get Reports
                  returns 200 Success response
        """
        response = self.stacktach_client.get_reports()
        self.assertEqual(response.status_code, 200,
                         self.msg.format("status code", "200",
                                         response.status_code, response.reason,
                                         response.content))
        self.assertGreaterEqual(len(response.entity), 1,
                                msg="The response content is blank")
        for element in response.entity:
            self.assertIsNotNone(element.report_id)
            self.assertIsNotNone(element.start)
            self.assertIsNotNone(element.end)
            self.assertIsNotNone(element.created)
            self.assertIsNotNone(element.name)
            self.assertIsNotNone(element.version)
