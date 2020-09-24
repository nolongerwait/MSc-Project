## eToxPred Datasets
- `fda_approved_nr.smi` - 1515 FDA-approved drugs obtained from DrugBank.
- `toxnet_nr.smi` - 3035 toxic molecules obtained from HSDB.
- `kegg_nr.smi` - 3682 drugs obtained from KEGG Drug.
- `t3db_nr.smi` - 1283 toxic molecules obtained from T3DB.
- `dude_actives_nr.smi` - 17499 bioactive molecules obtained from DUD-E.
- `nat_nubbe_nr.smi` - 1008 natural products obtained from NuBBE.
- `nat_unpd_nr.smi` - 81372 natural products obtained from UNPD.
- `tcm600_nr.smi` - 5883 traditional Chinese medicines obtained from Database@Taiwan.

## MoleculeNet Datasets
- `tox21_10k_challenge_test.smiles` - 296 drugs obtained from tox21 challenge used for test
- `tox21_10k_data_all.sdf` - 11764 drugs obtained from tox21 challenge 

***clintox***

```
The ClinTox dataset compares drugs approved by the FDA and drugs that have failed clinical trials for toxicity reasons. The dataset includes two classification tasks for 1491 drug compounds with known chemical structures: (1) clinical trial toxicity (or absence of toxicity) and (2) FDA approval status. List of FDA-approved drugs are compiled from the SWEETLEAD database, and list of drugs that failed clinical trials for toxicity reasons are compiled from the Aggregate Analysis of ClinicalTrials.gov(AACT) database.

The data file contains a csv table, in which columns below are used:
     "smiles" - SMILES representation of the molecular structure
     "FDA_APPROVED" - FDA approval status
     "CT_TOX" - Clinical trial results

And a smi file, in which stores the structure of these drugs.
```
- `clintox.csv`
- `clintox.smi`
- `CLINTOX_README`

***sider***
```
The Side Effect Resource (SIDER) is a database of marketed drugs and adverse drug reactions (ADR). The version of the SIDER dataset in DeepChem has grouped drug side effects into 27 system organ classes following MedDRA classifications measured for 1427 approved drugs.

The data file contains a csv table, in which columns below are used:
     "smiles" - SMILES representation of the molecular structure
     "Hepatobiliary disorders" ~ "Injury, poisoning and procedural complications" - Recorded side effects for the drug
	Please refer to http://sideeffects.embl.de/se/?page=98 for details on ADRs.

And a smi file, in which stores the structure of these drugs.
```
- `sider.csv`
- `sider.smi`
- `SIDER_README`

***tox21***
```
The “Toxicology in the 21st Century” (Tox21) initiative created a public database measuring toxicity of compounds, which has been used in the 2014 Tox21 Data Challenge. This dataset contains qualitative toxicity measurements for 8k compounds on 12 different targets, including nuclear receptors and stress response pathways.

The data file contains a csv table, in which columns below are used:
     "smiles" - SMILES representation of the molecular structure
     "NR-XXX" - Nuclear receptor signaling bioassays results
     "SR-XXX" - Stress response bioassays results
	please refer to the links at https://tripod.nih.gov/tox21/challenge/data.jsp for details.
And a smi file, in which stores the structure of these drugs.
```
- `tox21.csv`
- `tox21.smi`
- `TOX21_README`

***toxcast***
```
ToxCast is an extended data collection from the same initiative as Tox21, providing toxicology data for a large library of compounds based on in vitro high-throughput screening. The processed collection includes qualitative results of over 600 experiments on 8k compounds.


The data file contains a csv table, in which columns below are used:
     "smiles" - SMILES representation of the molecular structure
     "ACEA_T47D_80hr_Negative" ~ "Tanguay_ZF_120hpf_YSE_up" - Bioassays results
	please refer to the section "high-throughput assay information" at https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data for details.
And a smi file, in which stores the structure of these drugs.
```
- `toxcast_data.csv`
- `toxcast_data.smi`
- `TOXCAST_README`

## Neurotoxic Datasets
- `neurotoxic.smi` - 139 Neurotoxic agents, which have structure files, obtained from DrugBank, Accession Number: `DBCAT004545`

## Nephrotoxic Datasets
- `nephrotoxic.smi` - 218  Nephrotoxic agents, which have structure files, obtained from DrugBank, Accession Number: `DBCAT003959`

## Cardiotoxic Datasets
```
AMED Cardiotoxic Database is the database of small molecules which bind to various ion channels and potentially cause cardiotoxic risk.

The data file contains a tsv/csv table.
And a smi file, in which stores the structure of these drugs.
```
- `Cardiotoxic.csv`
- `Cardiotoxic.tsv`
- `Cardiotoxic.smi`

## Hepatotoxic Datasets
```
The DILIrank dataset is an updated version of the LTKB Benchmark dataset. DILIrank consists of 1,036 FDA-approved drugs that are divided into four classes according to their potential for causing drug-induced liver injury (DILI). The DILI classification is derived from analyzing the hepatotoxic descriptions presented in the FDA-approved drug labeling documents and assessing causality evidences in literature. Specifically, this largest publicly available annotated DILI dataset contains three groups (vMost-, vLess- and  vNo-DILI concern) with confirmed causal evidence linking a drug to liver injury, and one additional group (Ambiguous-DILI-concern) with causality undetermined.

     192 vMost-DILI-concern drug
     278 vLess-DILI-concern drug
     312 vNo-DILI-concern drug
     254 Ambiguous-DILI-concern drug
```

- `DILIrank-List.xlsx` Original database
- `DILIrank-List.csv` Exported csv file
- `DILIrank-List.smi` 721 drugs divided into three levels, representing Most-DILI-Concern, Less-DILI-Concern and No-DILI-Concern

## Genotoxic Datasets
```
OASIS genotoxicity database contains a large collection ofexperimental data (7404 entries) on chemicals for which information about different in vitro genotoxic effects (e.g., Ames test, chromosomal aberrations, mutagenicity in the mouse lymphoma assay) are available.
```
- `Genotoxicity OASIS.csv` Original database with only CAS number and SMILES columns
- `Genotoxicity OASIS.smi` 8031 drugs obtained from OASIS