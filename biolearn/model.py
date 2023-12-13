import pandas as pd
import numpy as np
from biolearn.util import get_data_file
from biolearn.dunedin_pace import dunedin_pace_normalization


def anti_trafo(x, adult_age=20):
    y = np.where(
        x < 0, (1 + adult_age) * np.exp(x) - 1, (1 + adult_age) * x + adult_age
    )
    return y


model_definitions = {
    "Horvathv1": {
        "year": 2013,
        "species": "Human",
        "tissue": "Multi-tissue",
        "source": "https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-10-r115",
        "output": "Age (Years)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "Horvath1.csv",
            "transform": lambda sum: anti_trafo(sum + 0.696),
        },
    },
    "Hannum": {
        "year": 2013,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.sciencedirect.com/science/article/pii/S1097276512008933",
        "output": "Age (Years)",
        "model": {"type": "LinearMethylationModel", "file": "Hannum.csv"},
    },
    "Lin": {
        "year": 2016,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.aging-us.com/article/100908/text",
        "output": "Age (Years)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "Lin.csv",
            "transform": lambda sum: sum + 12.2169841,
        },
    },
    "PhenoAge": {
        "year": 2018,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.aging-us.com/article/101414/text",
        "output": "Age (Years)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "PhenoAge.csv",
            "transform": lambda sum: sum + 60.664,
        },
    },
    "Horvathv2": {
        "year": 2018,
        "species": "Human",
        "tissue": "Skin + blood",
        "source": "https://www.aging-us.com/article/101508/text",
        "output": "Age (Years)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "Horvath2.csv",
            "transform": lambda sum: anti_trafo(sum - 0.447119319),
        },
    },
    "PEDBE": {
        "year": 2019,
        "species": "Human",
        "tissue": "Buccal",
        "source": "https://www.pnas.org/doi/10.1073/pnas.1820843116",
        "output": "Age (Years)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "PEDBE.csv",
            "transform": lambda sum: anti_trafo(sum - 2.1),
        },
    },
    "Zhang_10": {
        "year": 2019,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.nature.com/articles/ncomms14617",
        "output": "Mortality Risk",
        "model": {"type": "LinearMethylationModel", "file": "Zhang_10.csv"},
    },
    "DunedinPoAm38": {
        "year": 2020,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://elifesciences.org/articles/54870#s2",
        "output": "Aging Rate (Years/Year)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "DunedinPoAm38.csv",
            "transform": lambda sum: sum - 0.06929805,
        },
    },
    "DunedinPACE": {
        "year": 2022,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.proquest.com/docview/2634411178",
        "output": "Aging Rate (Years/Year)",
        "model": {
            "type": "LinearMethylationModel",
            "file": "DunedinPACE.csv",
            "transform": lambda sum: sum - 1.949859,
            "preprocess": dunedin_pace_normalization,
        },
    },
    "GrimAgeV1": {
        "year": 2019,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6366976/",
        "output": "Mortality Adjusted Age (Years)",
        "model": {
            "type": "NotImplemented",
            "file": "GrimAgeV1.csv"
        },
    },
    "GrimAgeV2": {
        "year": 2022,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9792204/",
        "output": "Mortality Adjusted Age (Years)",
        "model": {
            "type": "NotImplemented",
            "file": "GrimAgeV2.csv"
        },
    },
    "AlcoholMcCartney": {
        "year": 2018,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6158884/",
        "output": "Alcohol Consumption",
        "model": {"type": "LinearMethylationModel", "file": "Alcohol.csv"},
    },
    "BMI_McCartney": {
        "year": 2018,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6158884/",
        "output": "BMI",
        "model": {"type": "LinearMethylationModel", "file": "BMI.csv"},
    },
    "DNAmTL": {
        "year": 2019,
        "species": "Human",
        "tissue": "Blood, Adipose",
        "source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6738410/",
        "output": "Telomere Length",
        "model": {
            "type": "LinearMethylationModel",
            "file": "DNAmTL.csv",
            "transform": lambda sum: sum - 7.924780053,
        },
    },
    "HRSInCHPhenoAge": {
        "year": "2022",
        "species": "Human",
        "tissue": "Blood",
        "output": "Age (Years)",
        "source": "https://www.nature.com/articles/s43587-022-00248-2",
        "model": {
            "type": "LinearMethylationModel",
            "file": "HRSInCHPhenoAge.csv",
            "transform": lambda sum: sum + 52.8334080,
        },
    },
    "Knight": {
        "year": 2016,
        "species": "Human",
        "tissue": "Cord Blood",
        "source": "https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1068-z",
        "output": "Gestational Age",
        "model": {
            "type": "LinearMethylationModel",
            "file": "Knight.csv",
            "transform": lambda sum: sum + 41.7,
        },
    },
    "LeeControl": {
        "year": 2019,
        "species": "Human",
        "tissue": "Placenta",
        "source": "https://www.aging-us.com/article/102049/text",
        "output": "Gestational Age",
        "model": {
            "type": "LinearMethylationModel",
            "file": "LeeControl.csv",
            "transform": lambda sum: sum + 13.06182,
        },
    },
    "LeeRefinedRobust": {
        "year": 2019,
        "species": "Human",
        "tissue": "Placenta",
        "source": "https://www.aging-us.com/article/102049/text",
        "output": "Gestational Age",
        "model": {
            "type": "LinearMethylationModel",
            "file": "LeeRefinedRobust.csv",
            "transform": lambda sum: sum + 30.74966,
        },
    },
    "LeeRobust": {
        "year": 2019,
        "species": "Human",
        "tissue": "Placenta",
        "source": "https://www.aging-us.com/article/102049/text",
        "output": "Gestational Age",
        "model": {
            "type": "LinearMethylationModel",
            "file": "LeeRobust.csv",
            "transform": lambda sum: sum + 24.99772,
        },
    },
    "SmokingMcCartney": {
        "year": 2018,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6158884/",
        "output": "Smoking Status",
        "model": {"type": "LinearMethylationModel", "file": "Smoking.csv"},
    },
    "SexEstimation": {
        "year": 2021,
        "species": "Human",
        "tissue": "Blood",
        "source": "https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-021-07675-2",
        "output": "Sex",
        "model": {"type": "SexEstimationModel", "file": "estimateSex.csv"},
    },
}



class LinearMethylationModel:
    def __init__(
        self, coeffecient_file, transform, preprocess=None, **metadata
    ) -> None:
        self.transform = transform
        self.coefficients = pd.read_csv(
            get_data_file(coeffecient_file), index_col=0
        )
        self.preprocess = preprocess
        self.metadata = metadata

    @staticmethod
    def from_definition(clock_definition):
        def no_transform(_):
            return _

        model_def = clock_definition["model"]
        return LinearMethylationModel(
            model_def["file"],
            model_def.get("transform", no_transform),
            model_def.get("preprocess", no_transform),
            **{k: v for k, v in clock_definition.items() if k != "model"},
        )

    def predict(self, geo_data):
        dnam_data = self.preprocess(geo_data.dnam)

        # Join the coefficients and dnam_data on the index
        methylation_df = self.coefficients.join(dnam_data, how="inner")

        # Vectorized multiplication: multiply CoefficientTraining with all columns of dnam_data
        result = (
            methylation_df.iloc[:, 1:]
            .multiply(methylation_df["CoefficientTraining"], axis=0)
            .sum(axis=0)
        )

        # Return as a DataFrame
        return result.apply(self.transform).to_frame(name='Predicted')

    def methylation_sites(self):
        return list(self.coefficients.index)


class SexEstimationModel():
    def __init__(self, coeffecient_file, **metadata):
        self.coefficients = pd.read_csv(
            get_data_file(coeffecient_file), index_col=0, low_memory=False
        )
        self.metadata = metadata

    @staticmethod
    def from_definition(clock_definition):
        # Implementation for creating an instance from a definition
        # Adjust this as needed for your specific definition format
        return SexEstimationModel(clock_definition["model"]["file"], **{k: v for k, v in clock_definition.items() if k != "model"})

    def predict(self, geo_data):
        dnam_data = geo_data.dnam
        # Find the common probes between the reference and the input data
        common_probes = dnam_data.index.intersection(self.coefficients.index)
        reference = self.coefficients.loc[common_probes]
        dnam_data = dnam_data.loc[common_probes]

        # Identify autosomes and calculate mean and standard deviation
        autosomes = reference.loc[~reference["CHR"].isin(["X", "Y"])].index
        d_mean = dnam_data.loc[autosomes].mean(axis=0, skipna=True)
        d_std = dnam_data.loc[autosomes].std(axis=0, skipna=True)

        # Normalize the data using Z-score normalization
        z_data = dnam_data.subtract(d_mean, axis=1).div(d_std, axis=1).fillna(0)

        # Perform the sex prediction for chromosomes X and Y separately
        pred_xy = {}
        for chr in ["X", "Y"]:
            chr_ref = reference.loc[reference["pca"] == chr]
            pred = (z_data.loc[chr_ref.index].T - chr_ref["mean"].values).dot(
                chr_ref["coeff"].values
            )
            pred_xy[chr] = pred

        # Create a DataFrame from the prediction results
        pred_df = pd.DataFrame(pred_xy)

        # Map the prediction results to sex categories
        pred_df["predicted_sex"] = "Female"
        pred_df.loc[
            (pred_df["X"] < 0) & (pred_df["Y"] > 0), "predicted_sex"
        ] = "Male"
        pred_df.loc[
            (pred_df["X"] > 0) & (pred_df["Y"] > 0), "predicted_sex"
        ] = "47,XXY"
        pred_df.loc[
            (pred_df["X"] < 0) & (pred_df["Y"] < 0), "predicted_sex"
        ] = "45,XO"

        return pred_df

    def methylation_sites(self):
        return list(self.coefficients.index)

class ImputationDecorator:
    def __init__(self, clock, imputation_method):
        self.clock = clock
        self.imputation_method = imputation_method

    def predict(self, dnam_data):
        # Impute missing values before prediction
        needed_cpgs = self.clock.methylation_sites()
        dnam_data_imputed = self.imputation_method(dnam_data, needed_cpgs)
        return self.clock.predict(dnam_data_imputed)

    # Forwarding other methods and attributes to the clock
    def __getattr__(self, name):
        return getattr(self.clock, name)


def single_sample_clock(clock_function, data):
    return clock_function(data).iloc[0, 0]
