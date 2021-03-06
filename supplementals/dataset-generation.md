# Dataset generation

## XSEDE for running CD-HIT clustering
- location on XSEDE: `/pylon5/mc5fr5p/hbagheri/01_cdhit/cd-hit-v4.6.8-2017-1208/`

#### NR95
- nr95 size: 62G

Following is the job script to finish the nr95:

```text
[hbagheri@login018 cd-hit-v4.6.8-2017-1208]$ cat nr_job.sub 
#!/bin/bash
#BATCH -J nr95
#SBATCH -o nr95.o%j
#SBATCH -p LM
#SBATCH --mem=455G
#SBATCH -N 1
#SBATCH -n 28
#SBATCH -t 336:00:00
#SBATCH --mail-user=hbagheri@iastate.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --error=nr95.err
#SBATCH --output=nr95.out

cd /pylon5/mc5fr5p/hbagheri/01_cdhit/cd-hit-v4.6.8-2017-1208/
./cd-hit -i nr -o nr95 -c 0.95 -n 5 -g 1 -G 0 -aS 0.8  -d 0 -p 1 -T 28 -M 0 > nr95.log


```

run time:
```text
Slurm Job_id=10879225 Name=nr_job.sub Ended, Run time 20-16:15:09, COMPLETED, ExitCode 0

```

#### NR90

- nr90 size?
- important changes on Bridges for the LM jobs: Don't need `-n 28` any more.
- run time: `Slurm Job_id=11351220 Name=nr90_job_RM.sub Ended, Run time 7-14:37:38, COMPLETED, ExitCode 0`
Script to run the job on XSEDE
```text
[hbagheri@login018 cd-hit-v4.6.8-2017-1208]$ cat nr90_job.sub 
#!/bin/bash
#BATCH -J nr90
#SBATCH -o nr90.o%j
#SBATCH -p LM
#SBATCH --mem=455G
#SBATCH -N 1
#SBATCH -t 336:00:00
#SBATCH --mail-user=hbagheri@iastate.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --error=nr90.err
#SBATCH --output=nr90.out

cd /pylon5/mc5fr5p/hbagheri/01_cdhit/cd-hit-v4.6.8-2017-1208/
./cd-hit -i nr95 -o nr90 -c 0.90 -n 5 -g 1 -G 0 -aS 0.8  -d 0 -p 1 -T 28 -M 0 > nr90.log0

```


#### NR85
Script to run on the XSEDE supercomputer:
```text
#!/bin/bash
#BATCH -J nr85
#SBATCH -o nr85.o%j
#SBATCH -p RM
#SBATCH -N 1
#SBATCH -n 28
#SBATCH -t 72:00:00
#SBATCH --mail-user=hbagheri@iastate.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --error=nr85.err
#SBATCH --output=nr85.out

cd /pylon5/mc5fr5p/hbagheri/01_cdhit/cd-hit-v4.6.8-2017-1208
./cd-hit -i nr90 -o nr85 -c 0.85 -n 5 -g 1 -G 0 -aS 0.8 -d 0 -p 1 -T 28 -M 0 > nr85.log
```