import ROOT

def merge_root_files(input_files, output_file):
    outfile = ROOT.TFile(output_file, 'RECREATE')

    for filename in input_files:
        infile = ROOT.TFile(filename, 'READ')
        
        dirname = filename.split('_')[-1].replace('.root', '')
        
        outdir = outfile.mkdir(dirname)
        outdir.cd()
        
        for key in infile.GetListOfKeys():
            obj = key.ReadObj()
            if obj.InheritsFrom('TH1'):
                original_name = obj.GetName() 
                obj.SetDirectory(outdir)
                obj.SetName(original_name) 
                obj.Write()
        
        infile.Close()
    
    outfile.Write()
    outfile.Close()

input_files = [
    'dY_UL18_muon_0_500_CR1.root',
    'dY_UL18_muon_0_500_CR2.root',
    'dY_UL18_muon_0_500_SR.root'
]
output_file = 'dY_UL18_muon_0_500.root'

merge_root_files(input_files, output_file)
