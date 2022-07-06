import fire
import pandas as pd

import pyeuropeana.apis as apis
import pyeuropeana.utils as utils


def main(**kwargs):

    n_images_per_tier = kwargs.get('n_images_per_tier',100)
    saving_path = kwargs.get('saving_path')

    df = pd.DataFrame()
    for tier in range(3):

        resp = apis.search(
                query = '*',
                qf = f'(TYPE:IMAGE) AND (contentTier:{tier})',
                reusability = 'open AND permission',
                rows = n_images_per_tier
        )
        
        print(f'tier {tier}: {resp["totalResults"]} objects')
        _df = utils.search2df(resp)
        _df['tier'] = tier
        df = pd.concat([df,_df])

    df.to_csv(saving_path,index=False)

if __name__ == "__main__":
    fire.Fire(main)