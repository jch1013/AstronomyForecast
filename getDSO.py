"""
This script gets data on the rise and set times for galaxies and globular clusters and formats it into a report which
can be added to the body of the email response
"""
import DSO


def get_galaxies(html):
    galaxies = []
    all_galaxy_html = html.select(".lightgreybox")[4]
    all_galaxies = all_galaxy_html.findAll(lambda tag: tag.name == 'tr')
    for g in all_galaxies[2:]:
        galaxy_data = []
        for val in g:
            galaxy_data.append(val.text)
        new_galaxy = DSO.dso(galaxy_data[0], galaxy_data[1], galaxy_data[3], galaxy_data[2])
        galaxies.append(new_galaxy)
    return galaxies


def get_globluar_clusters(html):
    clusters = []
    all_cluster_html = html.select(".lightgreybox")[5]
    all_clusters = all_cluster_html.findAll(lambda tag: tag.name == 'tr')
    for c in all_clusters[2:]:
        cluster_data = []
        for val in c:
            cluster_data.append(val.text)
        new_galaxy = DSO.dso(cluster_data[0], cluster_data[1], cluster_data[3], cluster_data[2])
        clusters.append(new_galaxy)
    return clusters



def dso_report(html):
    report = ""

    # Add galaxies to report
    galaxies = get_galaxies(html)
    report += "\n-----Galaxies-----\n"
    for g in galaxies:
        report += str(g)
        report += "\n"

    # Add clusters to report
    clusters = get_globluar_clusters(html)
    report += "\n-----Globular Clusters-----\n"
    for c in clusters:
        report += str(c)
        report += "\n"
    return report
