import unittest;
import aluno as a;
import turma as t;

class turmaTest(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...')
    self.alunos = []
    
    self.alunos.append(a.Aluno('Fabio', 'Teixeira', 11))
    self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8))
    self.alunos.append(a.Aluno('Melissa', 'Teixeira', 6))    
    self.alunos.append(a.Aluno('Angela', 'Teixeira', -1))      
    
    self.turmaObject = t.Turma();
    self.turmaObject.cadastrarAlunos(self.alunos);
  
  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.')
  
  def testMaior(self):   
    self.assertEqual(11, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota')
    
  def testMenor(self):    
    self.assertEqual(-1, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota')

  def testIntervalo(self):
    for aluno in self.alunos:
      self.assertGreaterEqual(aluno.nota, 0, 'Nota abaixo de 0 encontrada')
      self.assertLessEqual(aluno.nota, 10, 'Nota acima de 10 encontrada')


if __name__ == "__main__":
  unittest.main()