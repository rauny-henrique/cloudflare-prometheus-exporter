# -*- coding: utf-8 -*-

"""Top-level package for Prometheus Cloudflare Exporter."""

__author__ = """Observability :: TransfewrWise"""
__email__ = "observability@transferwise.com"
__version__ = "0.1.12"


class CloudflareGQLQuery:
    def __init__(self):
        self.accounts = {
            data_accounts = """query httpRequests1hGroups($accountTag: ACCOUNTTAG!, $datetime_gt: DATETIMEGT!, $datetime_lt: DATETIMELT!) {
            viewer {
                accounts (filter: {accountTag: $accountTag}) {
                httpRequests1hGroups(limit: 5, filter: { datetime_gt: $datetime_gt, datetime_lt: $datetime_lt}) {
                    dimensions {datetime}
                    sum {
                    requests,
                    cachedBytes,
                    cachedRequests,
                    bytes,
                    encryptedBytes,
                    encryptedRequests,
                    pageViews,
                    threats,
                    clientHTTPVersionMap{
                        clientHTTPProtocol,
                        requests
                    }
                    browserMap{
                        pageViews,
                        uaBrowserFamily
                    }
                    clientHTTPVersionMap{
                        clientHTTPProtocol,
                        requests
                    }
                    contentTypeMap{
                        bytes,
                        requests,
                        edgeResponseContentTypeName
                    }
                    countryMap{
                        clientCountryName,
                        requests,
                        threats,
                        bytes
                    }
                    ipClassMap{
                        ipType,
                        requests
                    }
                    threatPathingMap{
                        requests,
                        threatPathingName
                    }
                    responseStatusMap{
                        requests,
                        edgeResponseStatus
                    }
                    }
                    uniq{
                        uniques
                    }
                }
                }
            }
            }
            """
            "httpRequests1hGroups": "".join(line.rstrip().lstrip() for line in data_accounts),
        }
        data_zones_one = """query httpRequests1hGroups($zoneTag: ZONETAG!, $datetime_gt: DATETIMEGT!, $datetime_lt: DATETIMELT!) {
        viewer {
            zones (filter: {zoneTag: $zoneTag}) {
            httpRequests1hGroups(limit: 5, filter: { datetime_gt: $datetime_gt, datetime_lt: $datetime_lt}) {
                dimensions {datetime}
                sum {
                requests,
                cachedBytes,
                cachedRequests,
                bytes,
                encryptedBytes,
                encryptedRequests,
                pageViews,
                threats,
                clientHTTPVersionMap{
                    clientHTTPProtocol,
                    requests
                }
                browserMap{
                    pageViews,
                    uaBrowserFamily
                }
                clientHTTPVersionMap{
                    clientHTTPProtocol,
                    requests
                }
                contentTypeMap{
                    bytes,
                    requests,
                    edgeResponseContentTypeName
                }
                countryMap{
                    clientCountryName,
                    requests,
                    threats,
                    bytes
                }
                ipClassMap{
                    ipType,
                    requests
                }
                threatPathingMap{
                    requests,
                    threatPathingName
                }
                responseStatusMap{
                    requests,
                    edgeResponseStatus
                }
                }
                uniq{
                    uniques
                }
            }
            }
        }
        }
        """
        data_zones_two = """query httpRequests1mGroups($zoneTag: ZONETAG!, $datetime_gt: DATETIMEGT!, $datetime_lt: DATETIMELT!) {
        viewer {
            zones (filter: {zoneTag: $zoneTag}) {
            httpRequests1mGroups(limit: 5, filter: { datetime_gt: $datetime_gt, datetime_lt: $datetime_lt}) {
                dimensions {datetime}
                sum {
                requests,
                cachedBytes,
                cachedRequests,
                bytes,
                encryptedBytes,
                encryptedRequests,
                pageViews,
                threats,
                clientHTTPVersionMap{
                    clientHTTPProtocol,
                    requests
                }
                browserMap{
                    pageViews,
                    uaBrowserFamily
                }
                clientHTTPVersionMap{
                    clientHTTPProtocol,
                    requests
                }
                contentTypeMap{
                    bytes,
                    requests,
                    edgeResponseContentTypeName
                }
                countryMap{
                    clientCountryName,
                    requests,
                    threats,
                    bytes
                }
                ipClassMap{
                    ipType,
                    requests
                }
                threatPathingMap{
                    requests,
                    threatPathingName
                }
                responseStatusMap{
                    requests,
                    edgeResponseStatus
                }
                }
                uniq{
                    uniques
                }
            }
            }
        }
        }
        """
        self.zones = {
            "httpRequests1hGroups": "".join(line.rstrip().lstrip() for line in data_zones_one),
            "httpRequests1mGroups": "".join(line.rstrip().lstrip() for line in data_zones_two),
        }


def read_gql_query(query_file):
    query_path = "/app/cloudflare_exporter/gql/"
    query_file = query_path + query_file
    with open(query_file) as data:
        query = "".join(line.rstrip().lstrip() for line in data)
    return query


query = CloudflareGQLQuery()
