# coding: utf-8

"""
    OpenLigaDB-API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MatchResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'result_id': 'int',
        'result_name': 'str',
        'points_team1': 'int',
        'points_team2': 'int',
        'result_order_id': 'int',
        'result_type_id': 'int',
        'result_description': 'str'
    }

    attribute_map = {
        'result_id': 'resultID',
        'result_name': 'resultName',
        'points_team1': 'pointsTeam1',
        'points_team2': 'pointsTeam2',
        'result_order_id': 'resultOrderID',
        'result_type_id': 'resultTypeID',
        'result_description': 'resultDescription'
    }

    def __init__(self, result_id=None, result_name=None, points_team1=None, points_team2=None, result_order_id=None, result_type_id=None, result_description=None):  # noqa: E501
        """MatchResult - a model defined in Swagger"""  # noqa: E501
        self._result_id = None
        self._result_name = None
        self._points_team1 = None
        self._points_team2 = None
        self._result_order_id = None
        self._result_type_id = None
        self._result_description = None
        self.discriminator = None
        if result_id is not None:
            self.result_id = result_id
        if result_name is not None:
            self.result_name = result_name
        if points_team1 is not None:
            self.points_team1 = points_team1
        if points_team2 is not None:
            self.points_team2 = points_team2
        if result_order_id is not None:
            self.result_order_id = result_order_id
        if result_type_id is not None:
            self.result_type_id = result_type_id
        if result_description is not None:
            self.result_description = result_description

    @property
    def result_id(self):
        """Gets the result_id of this MatchResult.  # noqa: E501


        :return: The result_id of this MatchResult.  # noqa: E501
        :rtype: int
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this MatchResult.


        :param result_id: The result_id of this MatchResult.  # noqa: E501
        :type: int
        """

        self._result_id = result_id

    @property
    def result_name(self):
        """Gets the result_name of this MatchResult.  # noqa: E501


        :return: The result_name of this MatchResult.  # noqa: E501
        :rtype: str
        """
        return self._result_name

    @result_name.setter
    def result_name(self, result_name):
        """Sets the result_name of this MatchResult.


        :param result_name: The result_name of this MatchResult.  # noqa: E501
        :type: str
        """

        self._result_name = result_name

    @property
    def points_team1(self):
        """Gets the points_team1 of this MatchResult.  # noqa: E501


        :return: The points_team1 of this MatchResult.  # noqa: E501
        :rtype: int
        """
        return self._points_team1

    @points_team1.setter
    def points_team1(self, points_team1):
        """Sets the points_team1 of this MatchResult.


        :param points_team1: The points_team1 of this MatchResult.  # noqa: E501
        :type: int
        """

        self._points_team1 = points_team1

    @property
    def points_team2(self):
        """Gets the points_team2 of this MatchResult.  # noqa: E501


        :return: The points_team2 of this MatchResult.  # noqa: E501
        :rtype: int
        """
        return self._points_team2

    @points_team2.setter
    def points_team2(self, points_team2):
        """Sets the points_team2 of this MatchResult.


        :param points_team2: The points_team2 of this MatchResult.  # noqa: E501
        :type: int
        """

        self._points_team2 = points_team2

    @property
    def result_order_id(self):
        """Gets the result_order_id of this MatchResult.  # noqa: E501


        :return: The result_order_id of this MatchResult.  # noqa: E501
        :rtype: int
        """
        return self._result_order_id

    @result_order_id.setter
    def result_order_id(self, result_order_id):
        """Sets the result_order_id of this MatchResult.


        :param result_order_id: The result_order_id of this MatchResult.  # noqa: E501
        :type: int
        """

        self._result_order_id = result_order_id

    @property
    def result_type_id(self):
        """Gets the result_type_id of this MatchResult.  # noqa: E501


        :return: The result_type_id of this MatchResult.  # noqa: E501
        :rtype: int
        """
        return self._result_type_id

    @result_type_id.setter
    def result_type_id(self, result_type_id):
        """Sets the result_type_id of this MatchResult.


        :param result_type_id: The result_type_id of this MatchResult.  # noqa: E501
        :type: int
        """

        self._result_type_id = result_type_id

    @property
    def result_description(self):
        """Gets the result_description of this MatchResult.  # noqa: E501


        :return: The result_description of this MatchResult.  # noqa: E501
        :rtype: str
        """
        return self._result_description

    @result_description.setter
    def result_description(self, result_description):
        """Sets the result_description of this MatchResult.


        :param result_description: The result_description of this MatchResult.  # noqa: E501
        :type: str
        """

        self._result_description = result_description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MatchResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MatchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other