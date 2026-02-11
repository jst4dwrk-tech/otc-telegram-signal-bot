asset_scores = {}

def update_asset_score(asset, win):
    if asset not in asset_scores:
        asset_scores[asset] = 0

    asset_scores[asset] += 1 if win else -1


def is_asset_dirty(asset):
    return asset_scores.get(asset, 0) <= -3
