package dao;

import log.Log;
import model.Livro;

import javax.persistence.EntityManager;
import java.io.IOException;
import java.util.List;


public class LivroDAO {

    private EntityManager em;

    //Criando instância do logger
    Log meuLogger = new Log("Log.txt");

    //Contrutor por atribuir o EntityManager vindo como parâmetro para o atributo em da classe local
    public LivroDAO(EntityManager em) throws IOException {
        this.em = em;
    }

    //Método responsável por cadastrar um livro na base de dados
    public void cadastrar(Livro livro) {
        this.em.persist(livro);
        System.out.println("\nO " + livro + " foi criado com sucesso!\n");
    }
}