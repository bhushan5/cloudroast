"""
Copyright 2014 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cafe.drivers.unittest.decorators import tags
from cafe.drivers.unittest.issue import skip_open_issue

from cloudroast.cloudkeep.barbican.fixtures import ContainerFixture


class ContainersAPI(ContainerFixture):

    @tags(type='positive')
    @skip_open_issue('launchpad', '1344365')
    def test_create_empty_generic_container(self):
        """Covers creating an empty generic container."""
        container_resp = self.behaviors.create_container("empty_container",
                                                         "generic", [])
        self._check_container_create_response(container_resp)

    @tags(type='positive')
    @skip_open_issue('launchpad', '1344365')
    def test_create_generic_container(self):
        """Covers creating a container with one secret ref."""
        responses = self.behaviors.create_container_with_secret()
        secret_resp, container_resp = responses
        self._check_container_create_response(container_resp)

    @tags(type='positive')
    @skip_open_issue('launchpad', '1344365')
    def test_create_rsa_container(self):
        """Covers creating an rsa container with references to a public key,
        a private key, and a passphrase."""
        secret_urls = self.secret_behaviors.create_n_secrets(3)
        container_resp = self.behaviors.create_rsa_container("rsa_container",
                                                             secret_urls[0],
                                                             secret_urls[1],
                                                             secret_urls[2])
        self._check_container_create_response(container_resp)

    @tags(type='positive')
    def test_get_generic_container(self):
        """Covers getting a generic container with a single secret."""
        responses = self.behaviors.create_container_with_secret(
            name="test_container", secret_name="test_secret")
        secret_resp, container_resp = responses

        # grab the urls
        container_ref = container_resp.entity.reference
        secret_ref = secret_resp.ref

        get_resp = self.container_client.get_container(container_ref)
        returned_refs = get_resp.entity.secret_refs

        # Verify the response data
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.entity.name, "test_container")
        self.assertEqual(get_resp.entity.container_ref, container_ref)
        self.assertEqual(get_resp.entity.container_type, "generic")

        # Verify the secret refs in the response
        self.assertEqual(len(returned_refs), 1)
        self.assertEqual(returned_refs[0].name, "test_secret")
        self.assertEqual(returned_refs[0].ref, secret_ref)

    @tags(type='positive')
    def test_get_rsa_container(self):
        """Covers getting an rsa container."""
        secret_urls = self.secret_behaviors.create_n_secrets(3)
        container_resp = self.behaviors.create_rsa_container("rsa_container",
                                                             secret_urls[0],
                                                             secret_urls[1],
                                                             secret_urls[2])

        container_ref = container_resp.entity.reference
        get_resp = self.container_client.get_container(container_ref)
        returned_refs = get_resp.entity.secret_refs
        returned_names = [secret.name for secret in returned_refs]
        returned_urls = [secret.ref for secret in returned_refs]

        # Verify the response data
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.entity.name, "rsa_container")
        self.assertEqual(get_resp.entity.container_ref, container_ref)
        self.assertEqual(get_resp.entity.container_type, "rsa")

        # Verify the secret refs in the response
        self.assertEqual(len(returned_refs), 3)
        self.assertEqual(set(secret_urls), set(returned_urls))
        self.assertIn("private_key", returned_names)
        self.assertIn("public_key", returned_names)
        self.assertIn("private_key_passphrase", returned_names)

    @tags(type='positive')
    def test_list_containers(self):
        """Covers getting a list of containers."""
        for i in xrange(11):
            self.behaviors.create_container(
                "container{0}".format(i), "generic", [])

        get_resp = self.container_client.get_containers(limit=10)
        self._check_list_of_containers(resp=get_resp, limit=10)

    @tags(type='positive')
    def test_delete_container(self):
        """Covers deleting a container."""
        responses = self.behaviors.create_container_with_secret()
        secret_resp, container_resp = responses

        container_ref = container_resp.entity.reference
        del_resp = self.behaviors.delete_container(container_ref)
        self.assertEqual(del_resp.status_code, 204)
