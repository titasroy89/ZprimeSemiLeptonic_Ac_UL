import ROOT

def copy_histograms(input_files, output_file_path):
    output_file = ROOT.TFile(output_file_path, 'RECREATE')

    directories = {
        'dY_UL18_ele_500_750_CR1.root' : 'CR1',
        'dY_UL18_ele_500_750_CR2.root': 'CR2',
        'dY_UL18_ele_500_750_SR.root' : 'SR'
    }

    for input_file_name, dir_name in directories.items():
        input_file = ROOT.TFile(input_file_name, 'READ')
        if input_file.IsOpen():
            print("Processing file: {}".format(input_file_name))

            output_dir = output_file.mkdir(dir_name)
            output_dir.cd()

            for key in input_file.GetListOfKeys():
                obj = key.ReadObj()
                if obj.InheritsFrom('TH1'):
                    hist = obj.Clone()
                    hist.Write()

            input_file.Close()
        else:
            print("Failed to open file: {}".format(input_file_name))

    output_file.Write()
    output_file.Close()

input_files = {
    'dY_UL18_ele_500_750_CR1.root' : 'CR1',
    'dY_UL18_ele_500_750_CR2.root': 'CR2',
    'dY_UL18_ele_500_750_SR.root' : 'SR'
}
output_file_path = 'dY_UL18_ele_500_750.root'

copy_histograms(input_files, output_file_path)
