#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Statuses(Service):
    """ Consume `Repo Statuses API
    <http://developer.github.com/v3/repos/statuses>`_ """

    def list(self, user=None, repo=None, sha=None):
        """ Get repository's collaborators

        :param str user: Username
        :param str repo: Repository
        :param str sha: Sha or branch to start listing commits from
        :returns: A :doc:`result`

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.statuses.list',
            user=user, repo=repo)
        params = {}
        params.update(sha and {'sha': sha} or {})
        return self._get_normal_result(request, **params)

    def add(self, collaborator, user=None, repo=None):
        """ Add collaborator to a repository

        :param str collaborator: Collaborator's username
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        .. warning::
            You must be authenticated and have perms in repository
        """
        request = self.make_request('repos.collaborators.add',
            collaborator=collaborator, user=user, repo=repo)
        return self._put(request)
