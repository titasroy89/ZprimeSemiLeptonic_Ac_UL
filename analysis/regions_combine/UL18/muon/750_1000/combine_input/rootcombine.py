import ROOT

def merge_root_files(input_files, output_file):
    outfile = ROOT.TFile(output_file, 'RECREATE')

    for filename in input_files:
        infile = ROOT.TFile(filename, 'READ')
        
        # Extract directory name from the file name (assuming format '..._CR1.root', etc.)
        dirname = filename.split('_')[-1].replace('.root', '')  # gets the part like 'CR1' from the filename
        
        outdir = outfile.mkdir(dirname)
        outdir.cd()
        
        for key in infile.GetListOfKeys():
            obj = key.ReadObj()
            if obj.InheritsFrom('TH1'):
                obj.SetDirectory(outdir)  
                obj.Write()
        
        infile.Close()
    
    outfile.Write()
    outfile.Close()

input_files = [
    'dY_UL18_muon_750_1000_CR1.root',
    'dY_UL18_muon_750_1000_CR2.root',
    'dY_UL18_muon_750_1000_SR.root'
]
output_file = 'dY_UL18_muon_750_1000.root'

merge_root_files(input_files, output_file)
